class CellularGrid extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <div>cellular-grid</div>
      `;
  }
}

customElements.define("cellular-grid", CellularGrid);
