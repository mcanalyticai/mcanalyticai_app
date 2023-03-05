import React from 'react';

// import illyc from '../../illyc.png';

import './SubBar.css';

export default function SubBar() {
    return (
        <div className="Total">
            <div className="container pt-3 pb-3">
                <div className="row SubBar">
                    <div className="col-md-4">
                        {/* <img className="logo" src={illyc} alt="Logo2" /> */}
                        <div className="row py-2">
                            <i class="fas fa-phone-alt mx-auto">
                                &nbsp;
                                (470) 981-4990
                            </i>
                        </div>
                        <div className="row py-2">
                            <i class="fas fa-envelope mx-auto">
                                &nbsp;
                                tech@mc-analyticai.com
                            </i>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="subbar-title">Our Services</div>
                        <a className="d-md-block " href="/web-dev">
                            Cybersecurity
                        </a>
                        <span className="d-inline-block d-md-none">&nbsp; | &nbsp;</span>

                        <a className="d-md-block" href="/data-analytics">
                            Encryption
                        </a>
                        <span className="d-inline-block d-md-none">&nbsp; | &nbsp;</span>

                    </div>

                    <div className="col-md-3">
                        <div className="subbar-title">Invest</div>
                        
                        <a className="d-md-block" href="/contact-form">
                            Contact form
                        </a>
                    </div>
                    <div className="col-md-2">
                        <div className="subbar-title">Get To Know Us</div>
                        <a className="d-md-block" href="/about">
                            About
                        </a>
                        <a className="d-md-block" href="/blog">
                            Blog
                        </a>
                    </div>
                </div>
            </div>
        </div>
    )
}