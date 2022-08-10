//Set element ID within HTML page where visitor count will be displayed
const countEl = document.getElementById('count');

//When calling the function, I accounted for successful completion and logging of any errors that may come up.
updateVisitCount()
	.then(response => {
		console.log('Updated visitor count successfully.')
	})
	.catch(error => {
		console.log('Function threw an error.')
		console.error(error)
	});

//This function fetches current visitor count from API (from DynamoDB database) and assigns it to the response variable.
//The response is then formatted as a JSON object and assigned to the data variable.
//For response, I used the await keyword to ensure the fetch action is complete before moving on in the code.
//For data, I used the await keyword to ensure that the response from the fetch is complete before attempting to format it as JSON.
//I then assigned the value of the JSON formatted visitor count from the API to the 'count' element within my HTML.
//https://api.countapi.xyz/update/brandon-daley/resume/?amount=1
async function updateVisitCount() {
	const response = await fetch('https://oki1grxc66.execute-api.us-east-1.amazonaws.com/count');
	const data = await response.json();
	countEl.innerHTML = data;
}