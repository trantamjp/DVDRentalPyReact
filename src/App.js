import React from 'react';
import Navigation from './components/Main';
import styled from 'styled-components'

const Styles = styled.div`
  margin: 0 auto;
  padding: 20px;

`

const App = () => (
  <Styles>
    <h1>Python Flask-SQLAlchemy-React Demo</h1>
    <Navigation />
  </Styles>
);


export default App;
