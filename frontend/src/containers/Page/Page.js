import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import Home from '../Home/Home';
import Services from '../Services/Services';
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
      <div>
        <Route exact path="/home" component={ Home } />
        <Route exact path="/services" component={ Services } />
        <Route exact path="/data-analytics" component={ WebDevelopment } />
        <Route exact path="/web-development" component={ DataAnalytics } />
        <Route exact path="/invest" component={ Invest } />
        <Route exact path="/comp-prob" component={ CompProb } />
        <Route exact path="/Other" component={ Other } />
        <Route exact path="/contact-invest" component={ ContactInvest } />
        <Route exact path="/about" component={ About } />
        <Route exact path="/blog" component={ Blog } />
        <Route exact path="/contact" component={ Contact } />
      </div>
    </BrowserRouter>
  )
}