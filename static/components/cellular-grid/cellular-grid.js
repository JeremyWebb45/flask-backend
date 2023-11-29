class CellularGrid {
  startState;
  startSelection;
  goalState;
  goalSelection;
  gridState = 'select start state';
  gridBody;
  gridSubmit;
  densitySlider;
  densityAmount;
  constructor() {
    this.gridBody = document.getElementById('gridBody');
    this.densitySlider = document.getElementById('densitySlider');
    this.densityAmount = document.getElementById('densityAmount');
    this.gridSubmit = document.getElementById('gridSubmit');
    this.startSelection = document.getElementById('startSelection');
    this.goalSelection = document.getElementById('goalSelection');
    this.attachListeners();
  }

  attachListeners() {
    this.gridBody.addEventListener('click', e => {
      const x = e.target.cellIndex;
      const y = e.target.parentElement.sectionRowIndex;
      const cellRender = `(${x}, ${y})`;
      const gridState = document.getElementById('gridState');
      switch (this.gridState) {
        case 'select start state':
          if (this.startState) {
            this.startState.className = '';
          }
          this.startState = e.target;
          e.target.className = 'startSelected';
          this.startSelection.innerHTML = cellRender;
          this.gridState = 'select goal state';
          gridState.innerHTML = this.gridState;
          break;
        case 'select goal state':
          if (this.goalState) {
            this.goalState.className = '';
          }
          this.goalState = e.target;
          e.target.className = 'goalSelected';
          this.goalSelection.innerHTML = cellRender;
          this.gridState = 'select obstacle density';
          this.densitySlider.disabled = false;
          this.gridSubmit.disabled = false;
          gridState.innerHTML = this.gridState;
          break;
        default:
          break;
      }
    });
    this.densitySlider.addEventListener('input', () => {
      this.densityAmount.innerHTML = this.densitySlider.value;
    });
    this.gridSubmit.addEventListener('click', () => {
      let data = new FormData();
      data.append('goal', this.goalSelection.innerHTML);
      data.append('start', this.startSelection.innerHTML);
      data.append('density', this.densityAmount.innerHTML);
      console.log(data);
      fetch('/api/path-planning', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: {
          start: this.startSelection.innerHTML,
        },
      })
        .then(res => {
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        });
    });
  }
}

new CellularGrid();
