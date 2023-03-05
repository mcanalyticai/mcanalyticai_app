import React from 'react';

import './Footer.css';


export default function Footer() {
    return (
        <div className="bg-dark">
            <div className="Footer container px-0 pt-2">
                <div className="row">

                    <div className="col-md-6 my-3" >
                        Copyright &copy;
                        mC_analyticAi
                        2023
                        &nbsp; <span>•</span> &nbsp; 
                        V 2.0.0
                        &nbsp; <span>•</span> &nbsp;
                        <a>Privacy</a>
                    </div>

                    <div className="col offset-2">

                        <div className="row">
                            <div className="col-3">
                                <i class="fab fa-linkedin social fa-3x"></i>
                            </div>
                            <div className="col-3">
                                <i class="fab fa-instagram-square fa-3x"></i>
                            </div>
                            <div className="col-3">
                                <i class="fas fa-comments fa-3x"></i>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>
    )
}