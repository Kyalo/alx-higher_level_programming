#!/usr/bin/node

process.argv.forEach((val, index) => {
	if (index == 1){
		console.log("No argument");
	}
	else if(index == 2){
		console.log("Argument found");
	}
	else if(index > 2){
		console.log("Arguments found");
	}
});
