import {Form} from 'react-bootstrap'
import React from 'react'
import { Button } from 'bootstrap'
import {Nav,Navbar,Container,NavDropdown} from 'react-bootstrap'
import { Route,Routes,BrowserRouter, NavLink} from 'react-router-dom'
export const Login = () => {
    return (
        <div className='container'>
            <h1>Login</h1>
            <Form>
  <Form.Group className="mb-3" controlId="formBasicEmail">
    <Form.Label>Email address</Form.Label>
    <Form.Control type="email" placeholder="Enter email" />
    <Form.Text className="text-muted">
      We'll never share your email with anyone else.
    </Form.Text>
  </Form.Group>

  <Form.Group className="mb-3" controlId="formBasicPassword">         
    <Form.Label>Password</Form.Label>         
    <Form.Control type="password" placeholder="Password" />         
  </Form.Group>         
  <Form.Group className="mb-3" controlId="formBasicCheckbox">         
    <Form.Check type="checkbox" label="Check me out" />         
  </Form.Group>         
  <button variant="primary"  className= 'btn btn-primary'type="submit">         
    Submit         
  </button>         
</Form>         
                     
        </div>         
    )         
}         
