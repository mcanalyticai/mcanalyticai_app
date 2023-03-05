import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

import './Posting.css';

export default function Posting(props) {
  const {message} = props;

  return (
      <div className="Posting internal-promo">
        <div className="container">
          <div className="message">{message}</div>
          <Link to="/contact">
            <br></br><br></br>
            <button className="btn btn-white">Job Contact Form</button>
          </Link>
        </div>
      </div>
  );
}

Posting.propTypes = {
  message: PropTypes.string
};