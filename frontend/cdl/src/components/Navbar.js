import React from "react";
import "./styles/Navbar.css";
import { Link } from 'react-router-dom';
export default function Navbar() {
    return (
        <nav
            className="navbar navbar-expand-lg custom-white-navbar sticky-top"
            style={{ backgroundColor: '#01080cff' }}
        >


            <div className="container-fluid">
                {/* Logo on the left */}
                <Link className="navbar-brand ms-5" to="/">
                    <img
                        src="/images/logo.png"
                        alt="Cosmic Logo"
                        height="50"
                        width="100"
                        className="d-inline-block align-text-top"
                    />
                </Link>

                {/* Toggler for mobile */}
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                {/* Nav items aligned right */}
                <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
                    <ul className="navbar-nav mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link className="nav-link" to="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#about">About Us</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}