// Get elements from the DOM
const generateButton = document.querySelector('#generate-btn');
const list1 = document.querySelector('#list-1');
const list2 = document.querySelector('#list-2');
const triesElement = document.querySelector('#tries');

// Calculate Pearson's r
function calculateCorrelation(x, y) {
  return jStat.corrcoeff(x, y);
}

// Generate a random list of 12 integers from 1 to 5
function generateList() {
  newList = [];

  // Repeat 12 times
  for (let i = 0; i < 12; i++) {
    // Generate a random integer from 1 to 5
    newList.push(Math.floor(Math.random() * 5) + 1);
  }

  return newList;
}

// Generate two lists with no correlation
function generateZeroR() {
  validLists = false;

  // Create lists
  let x;
  let y;

  // Store number of tries until successful lists are generated
  let tries = 0;

  while (!validLists) {
    // Generate two random lists
    x = generateList();
    y = generateList();

    // Increment tries
    tries++;

    // Check if they have no correlation
    if (calculateCorrelation(x, y) === 0) {
      validLists = true;
    }
  }

  return { x, y, tries };
}

// Plot graph of y vs x
function plotGraph(x, y) {
  const trace1 = {
    x,
    y,
    mode: 'markers',
    marker: {
      size: 20,
      color: '#3388dc',
      line: {
        color: '#00152a',
        width: 2,
      },
    },
    type: 'scatter',
  };

  const data = [trace1];

  const layout = {
    margin: {
      l: 50,
      r: 20,
      b: 20,
      t: 20,
    },
  };

  const config = { responsive: true, staticPlot: true };

  Plotly.newPlot('chart', data, layout, config);
}

// Add event listener to the generate button
generateButton.addEventListener('click', () => {
  // Generate lists
  const { x, y, tries } = generateZeroR();

  // Output lists to the DOM
  list1.innerHTML = `x: ${x.join(', ')}`;
  list2.innerHTML = `y: ${y.join(', ')}`;

  // Output number of tries to the DOM
  triesElement.innerHTML = `Tries: ${tries}`;

  plotGraph(x, y);
});
