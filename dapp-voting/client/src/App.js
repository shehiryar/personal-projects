import React, { useEffect, useState } from "react";
import Web3 from "web3";
import "./App.css";
import Navbar from "./components/Navbar";
import Table from "./components/Table";
import Election from "./contracts/Election.json";
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
// import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import { set } from "mongoose";

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

const App = () => {
  //all the UI
  // input value
  const classes = useStyles();
  const [chooseid, setChooseid] = useState("");

  const handleChange = (e) => {
    setChooseid(e.target.value);
  };
  const [refresh, setrefresh] = useState(0);
  //input value

  //things related to web3
  let content;
  const [loading2, setloading2] = useState(false);
  const [account, setAccount] = useState("");
  const [loading, setLoading] = useState(true);
  const [Hello, setHello] = useState({});

  //states related to electioncontract
  const [Electioncontract, setElectioncontract] = useState();
  const [contractowner, setContractowner] = useState("");
  const [voted, setVoted] = useState(false);
  const [showlead, setShowLead] = useState(false);
  const [Candidates, setCandidates] = useState([]);
  const [candidateAddress, setCandidateAddress] = useState("");
  const [candidateName, setCandidateName] = useState("");
  const [leading, setLeading] = useState([]);

  const loadWeb3 = async () =>{
    if (window.ethereum){
    window.web3 = new Web3(window.ethereum)
    await window.ethereum.enable()
    } else if (window.web3){
      window.web3 = new Web3(window.web3.currentProvider)
    } else{
      window.alert("Non Ethereum Browser Detected")
    }
  }

  const loadBlockchainData = async () => {
    setLoading(true);
    if (typeof window.ethereum == "undefined") {
      return;
    }
    const web3 = window.web3;
    const accounts = await web3.eth.getAccounts();
    setAccount(accounts[0])

    const networkId = await web3.eth.net.getId();
    const networkData = Election.networks[networkId];
    console.log(networkId, networkData)

    if(networkData){
      const electionContract = new web3.eth.Contract(
        Election.abi,

        networkData.address
      );

      setElectioncontract(electionContract);

      const owner = await electionContract.methods.contractOwner().call();
      console.log(owner);
      setContractowner(owner);

      var x = await electionContract.methods.candidates_count().call();
      var arr = [];

      for (var i = 0; i < x; i++) {
        await electionContract.methods
          .Candidates(i)
          .call()
          .then((candidate) => {
            arr = [
              ...arr,
              { id: i + 1, name: candidate[0], votes: candidate[1] },
            ];
          });
      }
      setCandidates(arr);

      setLoading(false);
    } else {
      window.alert("the contract not deployed to detected network.");
      setloading2(true);
    }
  };

  const onclick = async (a) => {
    const web3 = new Web3(window.web3);
    await Hello.methods
      .setCompleted(a.toString())
      .send({ from: account })
      .once("recepient", (recepient) => {
        console.log("success");
      })
      .on("error", () => {
        console.log("error");
      });
  };

  const walletAddress = async () => {
    await window.ethereum.request({
      method: "eth_requestAccounts",
      params: [
        {
          eth_accounts: {},
        },
      ],
    });
    window.location.reload();
  };

  useEffect(() => {
    loadWeb3();
    loadBlockchainData();

    if (refresh == 1) {
      setrefresh(0);
      loadBlockchainData();
    }
  }, [refresh]);

  const addCandidate = async () => {
    console.log(candidateName, candidateAddress);

    try {
      await Electioncontract.methods
        .add_candidate(candidateAddress, candidateName)
        .send({ from: account })
        .then((a) => {
          let id = a.events.Regestering_candidate.returnValues.candidate_id;
          let nam = a.events.Regestering_candidate.returnValues.name;
          let vot = a.events.Regestering_candidate.returnValues.total_vote;
          setCandidates([...Candidates, { id: id, name: nam, votes: 0 }]);
        });
    } catch (err) {
      if (account == contractowner) {
        window.alert(
          "This action is not allowed because a candidate is already registered on this address"
        );
      } else {
        window.alert("Your are not authorised to perform this action");
      }
    }
    console.log(Candidates);
    setCandidateName("");
    setCandidateAddress("");
  };

  const givevote = async () => {
    try {
      let ChoiceId = chooseid - 1;
      await Electioncontract.methods
        .add_vote(ChoiceId)
        .send({ from: account })
        .then((a) => {
          let id_returned = a.events.Voted.returnValues.id;
          console.log(id_returned);
        });
      setVoted(!voted);
    } catch (err) {
      window.alert("You have already voted");
    }
  };

  const showLeader = async() => {
    try {
      await Electioncontract.methods.leader().send({from: account}).then((a) => {
        let votes = a.events.Leader.returnValues.highest_votes
        let name = a.events.Leader.returnValues.name
        setLeading({name: name, votes: votes});
        setShowLead(!showlead);
      })
      setShowLead(!showlead);
    } catch (err) {
      window.alert("Something went wrong");
    }
  };

  if (loading === true) {
    content = (
      <p className="text-center">
        Loading...{loading2 ? <div>loading....</div> : ""}
      </p>
    );
  } else {
    content = (
      <div className="app">
        <div className="table">
          <Table Candidates={Candidates} />
        </div>
        <div className="do_vote">
          <h3>Select a candidate and click the "VOTE" button</h3>
        </div>
        <div className="input_id">
          <FormControl className={classes.formControl}>
            <InputLabel id="demo-simple-select-label">Select ID</InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={chooseid}
              onChange={handleChange}
            >
              {
                Candidates.length !== 0 ? (
                  Candidates.map((candidate) => (
                    <MenuItem key={candidate.name} value={candidate.id}>
                      {candidate.id}
                    </MenuItem>
                  ))
                ) : (
                  <MenuItem value={0}>No candidate</MenuItem>
                )
              }
            </Select>
          </FormControl>
          <Button variant="contained" onClick={givevote}>
            VOTE
          </Button>
        </div>
        <div className="after_voting">
          {voted && <h6>THANK YOU FOR YOUR VOTE</h6>}
        </div>
        <div className="showinguser_address">
          <h4>Your Address: {account}</h4>
        </div>
        <hr className="news1" />
        <div className="lead_title">
          <h4>FIND THE LEADING CANDIDATE</h4>
          <Button variant="contained" onClick={showLeader}>
            LEADING CANDIDATE
          </Button>
        </div>
        {showlead && (
          <div className="leader_details">
            <p>Name: {leading.name}</p>
            <p>Votes: {leading.votes}</p>
          </div>
        )}

        {contractowner === account && (
          <div className="add_candidate" id="add">
            <h3>Enter the details of new candidate:-</h3>
            <form className="candidate_form">
              <TextField
                id="outlined-basic"
                label="Name"
                autoComplete="off"
                variant="outlined"
                value={candidateName}
                onChange={(e) => setCandidateName(e.target.value)}
              />
              <TextField
                id="outlined-basic"
                label="Address"
                variant="outlined"
                autoComplete="off"
                value={candidateAddress}
                onChange={(e) => setCandidateAddress(e.target.value)}
              />
            </form>
            <Button variant="contained" onClick={addCandidate}>
              SUBMIT
            </Button>
          </div>
        )}

      </div>
    );
  }
  
  return (
    <div>
      <Navbar account={contractowner} />

      {account == "" ? (
        <div className="container">
          {" "}
          Connect your wallet to application{"   "}{" "}
          <button onClick={walletAddress}>metamask</button>
        </div>
      ) : (
        content
      )}
      {/* {content} */}
    </div>
  );
};

export default App;
