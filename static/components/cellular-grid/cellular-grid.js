class CellularGrid extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <div>cellular-grid</div>
      `;
  }

  attributeChangedCallback(name, oldValue, newValue) {
    console.log(`Attribute ${name} has changed.`);
    console.log(newValue);
  }
}

customElements.define('cellular-grid', CellularGrid);
