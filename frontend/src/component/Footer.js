// import './src/App.css';
// import { FlexImage } from './FlexImage';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Button} from 'react-bootstrap'
import { Route,Routes,BrowserRouter, NavLink} from 'react-router-dom'
import {Nav,Navbar,Container,NavDropdown,Carousel} from 'react-bootstrap'
// import { Register } from './Register';
export const Footer = () => {
    return (
        <div>
            <footer>
        <div className='container' style = {{textAlign:'center'}}>
          Copy right 2021 @ All rights are reserved!
        </div>
      </footer>
        </div>
    )
}
