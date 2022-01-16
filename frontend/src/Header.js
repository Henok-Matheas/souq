import React from 'react'
import './Header.css'
import './bootstrap.min.css'
import { Button,Navbar, NavDropdown, Container,Nav, Form,FormControl} from 'react-bootstrap'
import { RemoveShoppingCartOutlined, Search, ShoppingBasket, ShoppingBasketRounded, ShoppingCartOutlined, ShoppingCartTwoTone } from '@material-ui/icons'




function Header() {
    return (
      <Navbar className='nav' bg="light" expand="lg">
  <Container fluid>
    <Navbar.Brand href="#"><strong>Souq</strong></Navbar.Brand>
    <Navbar.Toggle aria-controls="navbarScroll" />
    <Navbar.Collapse id="navbarScroll">
      <Nav
        className="me-auto my-2 my-lg-0"
        style={{ maxHeight: '100px' }}
        navbarScroll
      >
        <Nav.Link href="#action1" to>Home</Nav.Link>
        <NavDropdown title="SignIn" id="navbarScrollingDropdown">
          <NavDropdown.Item href="#action3">Sign In</NavDropdown.Item>
          <NavDropdown.Item href="#action4">New to souq ?, Register</NavDropdown.Item>
          <NavDropdown.Divider />
          <NavDropdown.Item href="#action5">
            About
          </NavDropdown.Item>
        </NavDropdown>
        
        
      </Nav>
      
    </Navbar.Collapse>
    <Form className="d-flex search">
        <FormControl
          type="search"
          placeholder="Search"
          className=""
          aria-label="Search"
        />
        <Button className='me-3' ><Search/></Button>
      </Form>
    <ShoppingCartTwoTone/>
  </Container>
</Navbar>
        
        
    )
}

export default Header
