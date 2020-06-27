import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import Home from './Home';
import CustomerTable from './Customer';
import FilmTable from './Film';

const APIBaseUrl = window.location.protocol + "//" + window.location.hostname + ":5003"
const CustomerAPI = APIBaseUrl + "/api/datatable/customers";
const FilmAPI = APIBaseUrl + "/api/datatable/films";

// const Home = () => (
//   <div className='home'>
//     <h1>Welcome to my portfolio website</h1>
//     <p> Feel free to browse around and learn more about me.</p>
//   </div>
// );

const Main = () => (
  <Switch>
    <Route exact path='/home' component={
      () => {
        return <Home CustomerAPI={CustomerAPI} FilmAPI={FilmAPI} />
      }
    }></Route>
    <Route exact path='/customers' component=
      {
        () => {
          return <CustomerTable fetchUrl={CustomerAPI} />
        }
      }>
    </Route>
    <Route exact path='/films' component=
      {
        () => {
          return <FilmTable fetchUrl={FilmAPI} />
        }
      }>
    </Route>
    <Redirect to='/home' />
  </Switch>
);

export default Main;
