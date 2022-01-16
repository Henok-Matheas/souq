import './App.css';
import { FlexImage } from './Components/FlexImage';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Button} from 'react-bootstrap'
import React from 'react'
import { Route,Routes,BrowserRouter, NavLink} from 'react-router-dom'
import {Nav,Navbar,Container,NavDropdown,Carousel} from 'react-bootstrap'
import { Register } from './Register';
import { NavBar } from './Components/NavBar';
import Slider from './Components/Slider';

export const Home = () => {
    return (
        <div>
            
     <NavBar/>
     <FlexImage/>
    <Slider/>
    <div className='container'>
        
           
      </div>
     
      {/* <Register/> */}
      <hr className='container'/>
      <footer>
        <div className='container' style = {{textAlign:'center'}}>
          Copy right 2021 @ All rights are reserved!
        </div>
      </footer>
        </div>
    )
}
export default Home;
