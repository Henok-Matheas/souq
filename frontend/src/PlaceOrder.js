import React from 'react'
import React from 'react'
export const PlaceOrder = () => {
    return (
        <div>
                 
		
		<div className="section">
			{/* <!-- container --> */}
			<div className="container">
				{/* <!-- row --> */}
				<div className="row">

					<div className="col-md-7">
						{/* <!-- Billing Details --> */}
						<div className="billing-details">
							<div className="section-title">
								<h3 className="title">Billing address</h3>
							</div>
							<div className="mb-3">
								<input className='form-control' type="text" name="first-name" placeholder="First Name"/>
							</div>
							<div className="mb-3">
								<input className='form-control' type="text" name="last-name" placeholder="Last Name"/>
							</div>
							<div className="mb-3">
								<input className='form-control' type="email" name="email" placeholder="Email"/>
							</div>
							<div className="mb-3">
								<input className='form-control' type="text" name="address" placeholder="Address"/>
							</div>
							<div className="mb-3">
								<input className='form-control' type="text" name="city" placeholder="City"/>
							</div>
							<div className="mb-3">
								<input className='form-control' type="text" name="country" placeholder="Country"/>
							</div>
							
							<div className="mb-3">
								<input className='form-control' type="tel" name="tel" placeholder="Telephone"/>
							</div>
							<div className="mb-3">
								<div className="input-checkbox">
									<input type="checkbox" id="create-account"/>
									<label htmlFor="create-account">
										<span></span>
										Create Account?
									</label>
									<div className="caption">
										<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.</p>
										<input className='form-control' type="password" name="password" placeholder="Enter Your Password"/>
									</div>
								</div>
							</div>
						</div>
						{/* <!-- /Billing Details --> */}

						{/* <!-- Shiping Details --> */}
						<div className="shiping-details">
							<div className="section-title">
								<h3 className="title">Shiping address</h3>
							</div>
							<div className="input-checkbox">
								<input type="checkbox" id="shiping-address"/>
								<label htmlFor="shiping-address">
									<span></span>
									Ship to a diffrent address?
								</label>
								<div className="caption">
									<div className="mb-3">
										<input className='form-control' type="text" name="first-name" placeholder="First Name"/>
									</div>
									<div className="mb-3">
										<input className='form-control' type="text" name="last-name" placeholder="Last Name"/>
									</div>
									<div className="mb-3">
										<input className='form-control' type="email" name="email" placeholder="Email"/>
									</div>
									<div className="mb-3">
										<input className='form-control' type="text" name="address" placeholder="Address"/>
									</div>
									<div className="mb-3">
										<input className='form-control' type="text" name="city" placeholder="City"/>
									</div>
									<div className="mb-3">
										<input className='form-control' type="text" name="country" placeholder="Country"/>
									</div>
									
									<div className="mb-3">
										<input className='form-control' type="tel" name="tel" placeholder="Telephone"/>
									</div>
								</div>
							</div>
						</div>
						{/* <!-- /Shiping Details --> */}

						{/* <!-- Order notes --> */}
						<div className="order-notes">
							<textarea className='form-control' placeholder="Order Notes"></textarea>
						</div>
						{/* <!-- /Order notes --> */}
					</div>

					{/* <!-- Order Details --> */}
					<div className="col-md-5 order-details">
						<div className="section-title text-center">
							<h3 className="title">Your Order</h3>
						</div>
						<div className="order-summary">
							<div className="order-col">
								<div><strong>PRODUCT</strong></div>
								<div><strong>TOTAL</strong></div>
							</div>
							<div className="order-products">
								<div className="order-col">
									<div>1x Product Name </div>
									<div>birr 980.00</div>
								</div>
								<div className="order-col">
									<div>2x Product Name Goes Here</div>
									<div>birr 980.00</div>
								</div>
							</div>
							<div className="order-col">
								<div>Shiping</div>
								<div><strong>FREE</strong></div>
							</div>
							<div className="order-col">
								<div><strong>TOTAL</strong></div>
								<div><strong className="order-total">birr 2940.00</strong></div>
							</div>
						</div>
						<div className="payment-method">
							<div className="input-radio">
								<input type="radio" name="payment" id="payment-1"/>
								<label htmlFor="payment-1">
									<span></span>
									Direct Bank Transfer
								</label>
								
							</div>
							<div className="input-radio">
								<input type="radio" name="payment" id="payment-2"/>
								<label htmlFor="payment-2">
									<span></span>
									Cheque Payment
								</label>
								
							</div>
							<div className="input-radio">
								<input type="radio" name="payment" id="payment-3"/>
								<label htmlFor="payment-3">
									<span></span>
									CBE
								</label>
								
							</div>
						</div>
						<div className="input-checkbox">
							<input type="checkbox" id="terms"/>
							<label htmlFor="terms">
								<span></span>
								I've read and accept the <a href="#">terms & conditions</a>
							</label>
						</div>
						<a href="#" className="btn btn-primary order-submit">Place order</a>
					</div>
					{/* <!-- /Order Details --> */}
				</div>
				{/* <!-- /row --> */}
			</div>
			{/* <!-- /container --> */}
		</div>
		{/* <!-- /SECTION --> */}

        <div/>
        </div>
    )
}
export default PlaceOrder;