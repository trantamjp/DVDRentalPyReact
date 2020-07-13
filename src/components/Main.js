import React from 'react';
import { NavLink, Switch, Route } from 'react-router-dom';
import styled from 'styled-components'

import Home from './Home';
import CustomerTable from './Customer';
import FilmTable from './Film';

const Styles = styled.div`
nav ul {
  list-style: none;
  display: flex;
  background-color: black;
  margin-bottom: 20px;
}

nav ul li {
  padding: 20px;
}

nav ul li a {
  color: white;
  text-decoration: none;
}

.current {
  border-bottom: 4px solid white;
}
`


const Navigation = () => (
  <Styles>
    <nav>
      <ul>
        <li><NavLink activeClassName="current" to='/home'>Home</NavLink></li>
        <li><NavLink activeClassName="current" to='/customers'>Customer</NavLink></li>
        <li><NavLink activeClassName="current" to='/films'>Film</NavLink></li>
      </ul>
    </nav>
    <Switch>
      <Route exact path='/customers' component={CustomerTable} />
      <Route exact path='/films' component={FilmTable} />
      {/* Anything else */}
      <Route component={Home} />
    </Switch>

  </Styles>
);

export default Navigation;
