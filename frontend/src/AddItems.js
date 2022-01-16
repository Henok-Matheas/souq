import {Form} from 'react-bootstrap'

import { Button } from 'bootstrap'
import {Nav,Navbar,Container,NavDropdown} from 'react-bootstrap'
import { Route,Routes,BrowserRouter, NavLink} from 'react-router-dom'
export const AddItems = () => {
    return (
        <div>
            <form className="was-validated">
  <div className="custom-control custom-checkbox mb-3">
    <input type="checkbox" className="custom-control-input" id="customControlValidation1" required/>
    <label className="custom-control-label" for="customControlValidation1">Check this custom checkbox</label>
    <div className="invalid-feedback">Example invalid feedback text</div>
  </div>

  <div className="custom-control custom-radio">
    <input type="radio" className="custom-control-input" id="customControlValidation2" name="radio-stacked" required/>
    <label className="custom-control-label" for="customControlValidation2">Toggle this custom radio</label>
  </div>
  <div className="custom-control custom-radio mb-3">
    <input type="radio" className="custom-control-input" id="customControlValidation3" name="radio-stacked" required/>
    <label className="custom-control-label" for="customControlValidation3">Or toggle this other custom radio</label>
    <div className="invalid-feedback">More example invalid feedback text</div>
  </div>

  <div className="form-group">
    <select className="custom-select" required>
      <option value="">Open this select menu</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
      <option value="4">Three</option>
      <option value="5">Three</option>
    </select>
    <div className="invalid-feedback">Example invalid custom select feedback</div>
  </div>

  <div className="custom-file">
    <input type="file" className="custom-file-input" id="validatedCustomFile" required/>
    <label className="custom-file-label" for="validatedCustomFile">Choose file...</label>
    <div className="invalid-feedback">Example invalid custom file feedback</div>
  </div>
</form>
        </div>
    )
}
