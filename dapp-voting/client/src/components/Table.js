import React, { useState } from "react";
import "./Table.css";
import MaterialTable from "material-table";
import Check from "@material-ui/icons/Check";
import Clear from "@material-ui/icons/Clear";

export default function Table({ Candidates }) {
  // const [select, setSelect] = useState(false);
  // var icons;
  // select == false ? (icons = Clear) : (icons = Check);
  const mapedData =() =>{
    Candidates.map((i) => {
     return [{ SNo: i.id, name: i.name, vote: "10" }]
    })
  }

  return (
    <div className="table_style">
      <MaterialTable
        columns={[
          { title: "ID.", field: "id" },
          { title: "Candidate Name", field: "name" },
          { title: "Total Votes", field: "votes" },
        ]}
        data={
          query =>
            new Promise((resolve, reject) => {
                // prepare your data and then call resolve like this:
                resolve({
                    data: Candidates,
                    totalCount: Candidates.length,
                });
            })
        }
        title="List of Candidates"
        options={{
          search: false,
          paging: false,
          sorting: false,
          // selection: true,
          rowStyle: { height: 39.5 },
        }}
        localization={{
          header: {
            actions: "Choose",
          },
        }
      }
      />
    </div>
  );
}
