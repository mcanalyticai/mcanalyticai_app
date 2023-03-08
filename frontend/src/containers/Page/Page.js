import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Home from '../Home/Home';
/* import Services from '../Services/Services'; */
import DataAnalytics from '../Services/DataAnalytics/DataAnalytics';
import WebDevelopment from '../Services/WebDevelopment/WebDevelopment';
import Invest from '../Invest/Invest';
import CompProb from '../Invest/CompProb';
import Other from '../Invest/Other';
import ContactInvest from '../Invest/ContactInvest';
import About from '../About/About';
import Blog from '../Blog/Blog';
import Contact from '../Contact/Contact';

import '../Home/Home.css';
import '../Services/Services.css';
import '../Invest/Invest.css';
import '../About/About.css';
import '../Contact/Contact.css';


export default function Page() {
  return (
    <BrowserRouter>
        <Routes>
          <Route exact path="/home" component={ Home } />
          
          <Route exact path="/data-analytics" component={ WebDevelopment } />
          
        </Routes>
    </BrowserRouter>
  )
}