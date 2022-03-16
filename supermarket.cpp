/* Done by 18040210 */

#include <iostream>
#include <string>
#include <iomanip>
#include <vector>
using namespace std;

/***********************************************
		GLOBAL VARIABLES
***********************************************/

const int arraySize = 10; // Since no more items are being added to the arrays, the size of the arrays remains constant
int i;
string barcode; // variable for the barcode to be entered
float totalPrice; // variable for total price of all purchased products
float cashPaid; // variable for money given by the customer
float changeGiven; // variable for processed change
string newCustomer; // variable for input y/n when asked if theres a new customer
char printReceipt;
vector<string> purchasedName; // vector created to store name of purchased item which is to then be displayed in the receipt
vector<string> purchasedBarcode; // vector created to store barcode of the purchased item which is to then be displayed in the receipt
vector<float> purchasedPrice; // vector created to store price of purchased item which is to then be displayed in the receipt
float totalPriceBought;

/***********************************************
		FUNCTION PROTOTYPES
***********************************************/

void welcomeMessage();
void itemsBought();
void billing();
void receipt();

/***********************************************
		LIST OF ARRAYS
***********************************************/


string listOfProducts[arraySize] = { "Milk",
									 "Bread",
									 "Chocolate",
									 "Towel",
									 "Toothpaste",
									 "Soap",
									 "Pen",
									 "Biscuits",
									 "Lamp",
									 "Battery" };

string listOfBarcodes[arraySize] = { "0120001",
									 "0120002",
									 "0120003",
									 "0120004",
									 "0120005",
									 "0120006",
									 "0120007",
									 "0120008",
									 "0120009",
									 "0120010" };

float listOfPrices[arraySize] = { 10.50,
									 5.50,
									 8.00,
									 12.10,
									 6.75,
									 5.20,
									 2.00,
									 4.45,
									 20.50,
									 10.00 };

/***********************************************
		MAIN FUNCTION
***********************************************/
int main() {

	welcomeMessage();
	itemsBought();
	billing();
	receipt();
	// all of the above functions run in the main

	do {
		cout << "\nNew Customer?(y or n)" << endl;
		cin >> newCustomer;
		if (newCustomer == "y" || newCustomer == "Y") {
			purchasedBarcode.clear();
			purchasedPrice.clear();
			purchasedName.clear();
			// the data from the previous customers gets cleared inside the vectors

			welcomeMessage();
			itemsBought();
			billing();
			receipt();
			// the functions are run again
		}
		else {
			cout << "\nEnd of Program";
		}

	} while (newCustomer == "y" || newCustomer == "Y");
}// the loop above loops the whole program again while the input for new customer is 'y'

/***********************************************
		FUNCTION FOR WELCOME MESSAGE
***********************************************/

void welcomeMessage() {

	cout << "----------------------------------------------------" << endl;
	cout << "|   WELCOME TO HERTS SUPERMARKET CHECKOUT SYSTEM   |" << endl;
	cout << "| Scan the barcode or manually type the barcode ID |" << endl;
	cout << "----------------------------------------------------" << endl;
}

/***********************************************
		FUNCTION FOR ITEMS BOUGHT
***********************************************/

void itemsBought() {

	totalPrice = 0;// total price set to 0 because if no item is purchased, the program displays the total price as 0 and the user is not asked to enter any amount because nothing has been purchased

	do // Loop for the user to enter barcodes
	{
		cout << "\n\n" << "Please enter the barcode number of the purchased item (Type 'F' to finish):" << endl;
		cin >> barcode;

		bool invalidBarcode = true; // boolean value set for invalid barcode as true
		for (i = 0; i < 10; i++)
		{
			if (listOfBarcodes[i] == barcode) // if barcode entered exists in the array of barcodes
			{
				invalidBarcode = false; // boolean value is false since barcode entered exists in list of barcodes

				cout << "\n" << listOfProducts[i] << ", This item has been added to basket." << endl;

				cout << fixed;
				cout << "The price of this item is " << char(156) << setprecision(2) << listOfPrices[i] << endl;

				purchasedName.push_back(listOfProducts[i]);
				purchasedBarcode.push_back(listOfBarcodes[i]);
				purchasedPrice.push_back(listOfPrices[i]); // all entries are saved as vectors which are then to be used in the receipt

				totalPrice = totalPrice + listOfPrices[i]; // since total price was set to 0 earlier, it just adds the price of the item to itself over an over again until no items are left

				break; // stops the loop
			}
		}
		if (invalidBarcode == true && barcode != "F" && barcode != "f") { // if the boolean value is true i.e barcode does not exist and user does not end program, display error message
			cout << "Please enter a valid barcode" << endl;
		}
	} while (barcode != "F" && barcode != "f"); // the above loop occurs until 'f' is entered which ends the loop
}

/***********************************************
		FUNCTION FOR CALCULATIONS
***********************************************/
void billing() {

	float cashPaid;
	float changeGiven;
	cout << "\n\nTotal bill is " << setprecision(2) << char(156) << totalPrice << endl;

	do {
		if (totalPrice == 0) { // this statements checks if the program has ended without any barcode being entered which means total price will stay at 0
			cout << "Amount Paid: " << char(156) << "0.00" << endl;
		}
		else if (totalPrice > 0 || totalPrice < 0) { // this statement asks for money from the customer if barcodes have been entered so the total price has to be either greater than or less than 0
			cout << "\n\nAmount Paid: " << char(156);
			cin >> cashPaid;

			totalPrice = totalPrice - cashPaid;
		}
		.if (totalPrice > 0) { // if the total price is >0 then theres still some amount left to be paid
			cout << fixed;
			cout << "\n[!] INSUFFICIENT FUNDS! More cash needed: " << char(156) << setprecision(2) << totalPrice << endl;
		}
		else if (totalPrice < 0) { // if total price is <0 then extra money has been given so change has to be processed
			changeGiven = -totalPrice; // change is just how much extra money has been given, so '-' total price will be positive since negative-negative is positive

			cout << fixed;
			cout << "\nChange Given: " << setprecision(2) << char(156) << changeGiven << endl;
		}
		else if (totalPrice == 0) { // if exact amount is given then change is 0
			changeGiven = totalPrice;

			cout << fixed;
			cout << "Change Given: " << setprecision(2) << char(156) << changeGiven << endl;
		}
	} while (totalPrice > 0); // this gets looped until total is price is < or = 0
}

/***********************************************
		RECEIPT
***********************************************/
void receipt() {

	void billing();
	void itemsBought();
	float totalPriceBought; // total price calculation for the receipt
	totalPriceBought = 0;
	char printReceipt;

	cout << "\nWould you like to print a receipt? (enter 'y' to print and enter any other character for no)\n" << endl;
	cin >> printReceipt;

	if (printReceipt == 'y' || printReceipt == 'Y') {
		cout << setw(35) << "*****RECEIPT*****" << endl;
		cout << "|| ITEMS || " << setw(23) << " || BARCODES || " << setw(23) << " || PRICES || " << endl;

		for (int i = 0; i < purchasedName.size(); i++) // loops through all the vectors saved when entering data until no more vectors are left i.e all products purchased are displayed
		{
			cout << "\n" << purchasedName[i] << setw(30 - purchasedName[i].length()) << purchasedBarcode[i] << setw(18) << char(156) << purchasedPrice[i] << fixed << setprecision(2) << endl;
			totalPriceBought = totalPriceBought + purchasedPrice[i];
		}
	}
	else {
		cout << "\nNo receipt" << endl;
	}
	cout << "\nTotal Price: " << fixed << setprecision(2) << char(156) << totalPriceBought;
	cout << "\nChange Given: " << fixed << setprecision(2) << char(156) << -totalPrice << endl;
}

