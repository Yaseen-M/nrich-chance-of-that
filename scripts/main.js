// Get elements from the DOM
const generateButton = document.querySelector('#generate-btn');
const list1 = document.querySelector('#list-1');
const list2 = document.querySelector('#list-2');
const triesElement = document.querySelector('#tries');
const minSlider = document.querySelector('#min-slider');
const maxSlider = document.querySelector('#max-slider');
const minLabel = document.querySelector('#min-label');
const maxLabel = document.querySelector('#max-label');

// Store mix and max values
const boundary = {
  min: 1,
  max: 5,
};

// Generate random integer from min to max
function generateInt({ min, max }) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Generate a random list of 12 integers from min to max
function generateList() {
  newList = [];

  // Repeat 12 times
  for (let i = 0; i < 12; i++) {
    // Generate a random integer from min to max
    newList.push(generateInt(boundary));
  }

  return newList;
}

// Calculate Pearson's r
function calculateCorrelation(x, y) {
  return jStat.corrcoeff(x, y);
}

// Generate two lists with no correlation
function generateZeroR() {
  // Create lists
  let x;
  let y;

  // Store number of tries until successful lists are generated
  let tries = 0;

  validLists = false;

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

// Run when generate button is clicked
function generateButtonClick() {
  if (boundary.min < boundary.max) {
    // Generate lists
    const { x, y, tries } = generateZeroR();

    // Output lists to the DOM
    list1.innerHTML = `x: ${x.join(', ')}`;
    list2.innerHTML = `y: ${y.join(', ')}`;

    // Output number of tries to the DOM
    triesElement.innerHTML = `Tries: ${tries}`;

    plotGraph(x, y);
  }
}

// Run when min slider is updated
function minSliderUpdate() {
  boundary.min = parseInt(minSlider.value);
  minLabel.innerHTML = `Min: ${minSlider.value}`;
}

// Run when max slider is updated
function maxSliderUpdate() {
  boundary.max = parseInt(maxSlider.value);
  maxLabel.innerHTML = `Max: ${maxSlider.value}`;
}

// Add event listener to the generate button
generateButton.addEventListener('click', generateButtonClick);

// Add event listeners to the sliders
minSlider.addEventListener('input', minSliderUpdate);
maxSlider.addEventListener('input', maxSliderUpdate);

// Show initial mix and max slider values on the DOM
minSliderUpdate();
maxSliderUpdate();
