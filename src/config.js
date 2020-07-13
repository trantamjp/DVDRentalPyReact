const location = window.location;
const APIBASEURL = process.env.REACT_APP_APIBASEURL || `${location.protocol}//${location.host}`;

export const CUSTOMER_API_URL = APIBASEURL + "/api/datatable/customers";
export const FILM_API_URL = APIBASEURL + "/api/datatable/films";
