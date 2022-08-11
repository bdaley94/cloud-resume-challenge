//Set element ID within HTML page where visitor count will be displayed
const countEl = document.getElementById('count');

//When calling the function, I accounted for successful completion and logging of any errors that may come up.
updateVisitCount()
	.then(response => {
		console.log('updateVisitCount function completed without errors.')
	})
	.catch(error => {
		console.error('ERROR: updateVisitCount function threw an error.')
	});

//This function fetches current visitor count from API (from DynamoDB database) and assigns it to the response variable.
//The response is then formatted as a JSON object and assigned to the data variable.
//For response, I used the await keyword to ensure the fetch action is complete before moving on in the code.
//For data, I used the await keyword to ensure that the response from the fetch is complete before attempting to format it as JSON.
//I then assigned the value of the JSON formatted visitor count from the API to the 'count' element within my HTML.
async function updateVisitCount() {
	const response = await fetch('https://oki1grxc66.execute-api.us-east-1.amazonaws.com/count');
	const data = await response.json();	
	countEl.innerHTML = data;

	//This if statement performs some built-in testing. Specifically, it tests to make sure the API returns an expected value.
	//It also checks to make sure the webpage was actually updated with the returned value.
	//If both of these tests do not pass, it will log the error in the console.
	if (Number.isInteger(data) == true && countEl.innerHTML == data) {
		console.log('Updated visitor count on webpage successfully.');
	}
	else {
		console.error('ERROR: The API did not return an expected number value.')
	}
}