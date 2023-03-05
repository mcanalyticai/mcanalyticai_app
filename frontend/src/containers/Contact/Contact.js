import React from 'react';
import logo from '../../assets/imgs/logo.png';
import { LogicalNotInputs } from '@tensorflow/tfjs';
import './Contact.css';

function getCurrentURL() {
    // x = window.location.href
    console.log(window.location.href)
    return window.location.href
}
function storeData() {
    console.defaultLog = console.log.bind(console);
    console.logs = [];
    console.log = function() {
        // default &  console.log()
        console.defaultLog.apply(console, arguments);
        // new & array data
        console.logs.push(Array.from(arguments));
    }
}
function submit() {
    getCurrentURL()
    storeData()
}
export default function Contact(getCurrentURL) {
    return (
        <div>
            <div className="Break-Div-Top bg-dark"></div>
            
        
            <div className="Contact ml-5 mr-5 pt-3">
                <div className="container">
                    <div className="row">

                        {/* Contact Form */}
                        <div className="col-md-6">
                            <div className="ContactForm">
                                <form>

                                    <div className="form-group">
                                        <label className="h5 mb-2 form-label">Your Name</label>
                                        <div className="input-group">
                                            <div className="input-group-prepend">
                                                <span className="input-group-text">&nbsp;</span>
                                            </div>
                                            <input required placeholder="Enter Name" name="name"
                                            type="text" className="form-control" />
                                        </div>
                                    </div>
                                    <div className="form-group">
                                        <label className="h5 mb-2 form-label">Your Email</label>
                                        <div className="input-group">
                                            <div className="input-group-prepend">
                                                <span className="input-group-text">&nbsp;</span>
                                            </div>
                                            <input required placeholder="Enter Email" email="email"
                                            type="text" className="form-control" />
                                        </div>
                                    </div>
                                    <div className="form-group">
                                        <label className="h5 mb-2 form-label">Message</label>
                                        <div className="Text-Area input-group">
                                            <div className="input-group-prepend">
                                                <span className="input-group-text">&nbsp;</span>
                                            </div>
                                            <textarea required row="6" name="message" 
                                            className="for m-control"></textarea>
                                        </div>
                                    </div>
                                    <div className="mt-md-5 my-sm-4 row">
                                        {/* <div className="mb-sm-4 col-md-8 col-sm-12"></div> */}
                                        <div className="col-md-4 col-sm-12">
                                            <button type="submit" className="btn-dark btn-block
                                            btn btn-primary" onClick={console.log(getCurrentURL)}>Submit</button>
                                            
                                        </div>
                                        
                                    </div>

                                </form>
                            </div>
                        </div>

                        


                        {/* Information */}
                        <div className="col-md-6">
                            <img src={logo} alt="Logo" className="Logo-Contact mb-3"></img>

                            <h2>Atlanta Office</h2>

                            <hr></hr>
                            <p>
                                Phone: (470) 981-4990
                                <br></br>
                                Email: tech@mc-analyticai.com
                            </p>

                            <hr></hr>
                            <div className="d-flex justify-content-center">
                                <div className="pl-5">
                                    <i class="fab fa-linkedin-in fa-2x mr-3"></i>
                                </div>
                                <div className="pr-5">
                                    <i class="fab fa-instagram fa-2x ml-3"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="Break-Div-Bottom bg-dark"></div>
            
        </div>
        
    )
}