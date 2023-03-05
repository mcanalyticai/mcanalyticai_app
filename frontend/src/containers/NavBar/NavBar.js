import React from 'react';

import logo from '../../assets/imgs/logo.png';

export default function NavBar() {
    return (
        <div className="Bar">
            
            <div className="Top container">
                {/* Logo Name */}
                <div className="Top-Row row">
                    {/* <div className="Top-Logo col-2 mt-3" style={{minWidth: "130px"}}> 
                        <img src={logo} className="Top-Logo mx-auto" alt="Logo" />
                    </div> */}
                    <div className="col-6" style={{maxWidth: "350px"}}>
                        <img src={logo} className="Top-Name" alt="Name"/>
                    </div>
                </div>

                {/* NavBar */}
                <div className="NavBar">
                    <nav class="navbar navbar-expand-md navbar-light" >

                        <a class="navbar-brand" href="#"></a>
                            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                            </button>
                        <div class="collapse navbar-collapse" id="navbarNavDropdown">
                            <ul class="navbar-nav">
                                <li class="nav-item active">
                                    <a class="nav-link tab" href="/home">Home <span class="sr-only">(current)</span></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link tab" href="/services">Services</a>
                                </li>
                                <li class="nav-item dropdown">
                                    <a class="nav-link tab" href="/invest"  aria-haspopup="true" aria-expanded="false">
                                    Invest
                                    </a>
                                    {/* <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                        <a class="dropdown-item" href="/comp-prob">Computational probability model</a>
                                        <a class="dropdown-item" href="/other">Other softwares</a>
                                        <a class="dropdown-item" href="/contact-invest">Contact form</a>
                                    </div> */}
                                </li>
                                
                                &nbsp;
                                <div style={ {fontSize: "25px", color: "grey"} }>  | </div>
                                &nbsp;
                                
                                <li class="nav-item">
                                    <a class="nav-link tab" href="/about">About</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link tab" href="/blog">Blog</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link tab" href="/contact">Contact</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link tab" href="/search">Search</a>
                                </li>
                            </ul>
                        </div>

                    </nav>
                </div>

            </div>
        </div>
    );
}