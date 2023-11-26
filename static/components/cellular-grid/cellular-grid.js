class CellularGrid extends HTMLElement {
  grid;
  height;
  width;
  constructor() {
    super();
    const serverData = JSON.parse(this.getAttribute("data-"));
    this.grid = serverData.grid;
    this.height = serverData.height;
    this.width = serverData.width;
  }

  connectedCallback() {
    const gridContainer = document.createElement("table");
    const tBody = gridContainer.createTBody();
    this.grid.forEach((row, rowIdx) => {
      const currRow = document.createElement("tr");
      tBody.appendChild(currRow);
      row.forEach((cell, cellIdx) => {
        const currCell = document.createElement("td");
        currCell.addEventListener("click", () => {
          console.log("hey");
        });
        currRow.appendChild(currCell);
      });
    });
    this.innerHTML = gridContainer.outerHTML;
  }
}

customElements.define("cellular-grid", CellularGrid);
