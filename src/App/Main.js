import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import Home from './Home';
import CustomerTable from './Customer';
import FilmTable from './Film';

const APIBaseUrl = window.location.protocol + "//" + window.location.hostname + ":5004"
const CustomerAPI = APIBaseUrl + "/api/datatable/customers";
const FilmAPI = APIBaseUrl + "/api/datatable/films";

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
