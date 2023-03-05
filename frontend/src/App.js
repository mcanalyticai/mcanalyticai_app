import React from 'react';

import NavBar from './containers/NavBar/NavBar';
import Page from './containers/Page/Page';
import SubBar from './containers/SubBar/SubBar';
import Footer from './containers/Footer/Footer';

import './App.css';
import './containers/NavBar/NavBar.css';
import './containers/SubBar/SubBar.css';
import './containers/Footer/Footer.css';

function App() {
  return (
    <div className="App">
      <div>
        <NavBar></NavBar>
      </div>
      <div>
        <Page></Page>
      </div>
      <div>
        <SubBar></SubBar>
      </div>
      <div>
        <Footer></Footer>
      </div>
      
      
      {/*
      <header className="App-header"></header>
      */}
    </div>
  );
}

export default App;
