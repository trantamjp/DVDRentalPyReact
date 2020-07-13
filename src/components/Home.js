import React from 'react';
import styled from 'styled-components'

import { CUSTOMER_API_URL, FILM_API_URL } from '../config';

const Styles = styled.div`
span.link {
    cursor: pointer;
    text-decoration: underline;
}
`

const Home = () => (
    <Styles>
        <h2>Github</h2>
        <a href="https://github.com/trantamjp/DVDRentalPyReact" target="_blank" rel="noopener noreferrer">
            https://github.com/trantamjp/DVDRentalPyReact</a>
        <h2>Sample Data</h2>
        <h4>Download from here <a href="https://www.postgresqltutorial.com/postgresql-sample-database/" target="_blank" rel="noopener noreferrer">
            https://www.postgresqltutorial.com/postgresql-sample-database/</a></h4>
        <p>Please click the link from the top menu</p>
        <ol>
            <li>
                <p>Customer List</p>
                <p>DataTable with server-side processing, pulling customer data from the API located at <strong>{CUSTOMER_API_URL}</strong>
                </p>
            </li>
            <li>
                <p>Films List</p>
                <p>DataTable with server-side processing, pulling customer data from the API located at <strong>{FILM_API_URL}</strong>
                </p>
            </li>
        </ol>
    </Styles>
);

export default Home;
