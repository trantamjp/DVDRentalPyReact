import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import CustomerTable from './Customer';
import FilmTable from './Film';

const APIBaseUrl = window.location.protocol + "//" + window.location.hostname + ":50041"
const CustomerAPI = APIBaseUrl + "/api/datatable/customers";
const FilmAPI = APIBaseUrl + "/api/datatable/films";

const redirectURL = window.location.protocol + "//" + window.location.hostname

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
    <Route exact path="/" render={() => (window.location = redirectURL)} />
  </Switch>
);

export default Main;
