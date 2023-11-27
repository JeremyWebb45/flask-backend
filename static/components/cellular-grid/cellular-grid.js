class CellularGrid extends HTMLElement {
  grid;
  height;
  width;
  tBody;
  constructor() {
    super();
    const serverData = JSON.parse(this.getAttribute("data-"));
    this.grid = serverData.grid;
    this.height = serverData.height;
    this.width = serverData.width;
    this.tBody = document.getElementById("gridBody");
    console.log(this.tBody);
  }

  connectedCallback() {
    const gridContents = document.createElement("div");
    this.grid.forEach((row, rowIdx) => {
      const currRow = document.createElement("tr");
      gridContents.appendChild(currRow);
      row.forEach((cell, cellIdx) => {
        const currCell = document.createElement("td");
        currRow.appendChild(currCell);
      });
    });
    console.log(gridContents.innerHTML);
    this.innerHTML = gridContents.innerHTML;
  }
}

customElements.define("cellular-grid", CellularGrid);
