import 'bootstrap/dist/css/bootstrap.min.css'
import {Button} from 'react-bootstrap'
import { Route,Routes,BrowserRouter, NavLink} from 'react-router-dom'
import {Nav,Navbar,Container,NavDropdown,Carousel} from 'react-bootstrap'
// import { Register } from './Register';
function Slider() {
    return (
        <div>
            <Carousel>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src="https://i.pinimg.com/originals/b6/c9/17/b6c9173bd58f62f49eb550635a5e259f.jpg"
                alt="First slide" />
              <Carousel.Caption>
                <h3>First slide label</h3>
                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
              </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src="https://i.pinimg.com/originals/b6/c9/17/b6c9173bd58f62f49eb550635a5e259f.jpg"
                alt="Second slide" />

              <Carousel.Caption>
                <h3>Second slide label</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src="https://i.pinimg.com/originals/b6/c9/17/b6c9173bd58f62f49eb550635a5e259f.jpg"
                alt="Third slide" />

              <Carousel.Caption>
                <h3>Third slide label</h3>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
              </Carousel.Caption>
            </Carousel.Item>
          </Carousel>
        </div>
    )
}
export default Slider