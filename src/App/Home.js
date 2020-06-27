import React from 'react';

const Home = (props) => (
    <div>
        <h2>Github</h2>
        <a href="https://github.com/trantamjp/DVDRentalPyReact">https://github.com/trantamjp/DVDRentalPyReact</a>
        <h2>Sample Data</h2>
        <h3>Download from here <a href="https://www.postgresqltutorial.com/postgresql-sample-database/">https://www.postgresqltutorial.com/postgresql-sample-database/</a></h3>
        <ol>
            <li>
                <p>Customers List<br /><a href="/customers">Customer</a></p>
                <p>DataTable with server-side processing.<br />
                The API sample is <a href={props.CustomerAPI} target="_blank" rel="noopener noreferrer" >here</a> (Only first 10 rows).
                </p>
            </li>
            <li><p>Films List<br /><a href="/films">Film</a></p>
                <p>DataTable with server-side processing.<br />
                The API sample is <a href={props.FilmAPI} target="_blank" rel="noopener noreferrer" >here</a> (Only first 10 rows).
                </p>
            </li>
        </ol>
    </div>
);

export default Home;
