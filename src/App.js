import React from 'react';
import './App.css';
import Navigation from './AppNavigation';
import Main from './App/Main';

const App = () => (
  <div className='app'>
    <h1>Python + React Demo</h1>
    <Navigation />
    <Main />
  </div>
);


export default App;
