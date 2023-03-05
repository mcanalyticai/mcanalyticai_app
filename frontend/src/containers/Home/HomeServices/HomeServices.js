import React from 'react';

import Contact from '../../../components/Contact/Contact';

import DataAnalytics from '../../../components/DataAnalytics/DataAnalytics';
import WebDev from '../../../components/WebDev/WebDev';

import './HomeServices.css';

export default function HomeServices() {
    return (
        <div>
            <div className="Data-Analytics row justify-content-between home-services p-3">
                <div className="col">
                    <DataAnalytics></DataAnalytics>
                </div>
                <div className="col text-light description-data">
                    <h3>Cybersecurity</h3>   
                    <p className="mb-0 mx-auto">
                    
                    </p>
                    <br></br>
                    <button type="button" className="btn btn-light">
                        Data Analytics &nbsp;
                        <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
                
            </div>
            <div className="Web-Dev row justify-content-between home-services p-3">
                <div className="col text-light description-web">
                    <h3>Encryption</h3>
                    
                    <br></br>
                    <button type="button" className="btn btn-light">
                        Web Development &nbsp;
                        <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
                <div className="col">    
                    <WebDev></WebDev>
                </div>
            </div>

            {/* Contact component */}
            <Contact
                message="Looking for software for your business?"
            />

        </div>
    )
}