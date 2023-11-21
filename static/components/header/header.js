class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <header>
        <nav>
          <a href="about.html">
            <img src="static/favicon.ico" alt="logo icon" width="32" height="32"/>
            <p>ebbfolio</p>
          </a>
          <ul>
            <li><a href="data-science.html"><p>Data science</p></a></li>
            <li><a href="front-end.html"><p>Front end</p></a></li>
          </ul>
          <span />
        </nav>
      </header>
    `;
  }
}

customElements.define('header-component', Header);
