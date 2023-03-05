import React from 'react';

import Posting from '../../components/Posting/Posting';

import './About.css';

import President from '../../assets/imgs/President.png';




export default function About() {
    return (
        <div className="About">

            <div className="About-Header bg-dark">
                <h1>ABOUT</h1>
                <p>
                    who we are&nbsp; &#38; &nbsp;what we do
                </p>
            </div>

            <p className="Biz-Statement">
                Specializing in cybersecurity and encryption
                we're confident in meeting your business needs by making 
                valuable software applications and providing insightful
                analytics. Contact us for patent investments.
            </p>
            <p>
                
            </p>

            <hr></hr>

            <div className="About-Page container">
                <div className="row">
                    <div className="col-md-4 grey-box">
                        <img src={President} className="President" alt="President"></img>
                        <h3>Christian Adams</h3>
                        <p><em>President &#38; Chief Architect</em></p>
                    </div>
                </div>
            </div>

            <div>
            

  
            </div>

            <Posting
                message="Are you interesting in joining our team?"
            />
        </div>
    )
}