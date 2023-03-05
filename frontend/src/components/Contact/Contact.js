import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

import './Contact.css';

export default function ContactUs(props) {
  const {message} = props;

  return (
      <div className="ContactUs internal-promo">
        <div className="container">
          <div className="message">{message}</div>
          <Link to="/contact">
            <br></br><br></br>
            <button className="btn btn-white">Contact Us</button>
          </Link>
        </div>
      </div>
  );
}

ContactUs.propTypes = {
  message: PropTypes.string
};