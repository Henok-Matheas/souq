import React from "react";
import {
  Routes,Route,
  BrowserRouter
} from "react-router-dom";

import "./App.css";
import "./Header";
import Home from "./Home";
import Header from "./Header";
import Shop from "./Shop";
import Seller from "./Seller";
import ItemPage from "./ItemPage";
import Register from "./Register";
import AddItems from "./AddItems";
import { Login } from "./Login";
import PlaceOrder from "./PlaceOrder";

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={[<Header />,<Home/>] } />
      <Route path="/shop" element={[<Header />,<Shop/>] } />
      <Route path="/seller" element={[<Header />,<Seller/>] } />
      <Route path="/itempage" element={[<Header />,<ItemPage/>] } />
       <Route path="/register" element={[<Header />,<Register/>] } />
        <Route path="/AddItems" element={[<Header />,<AddItems/>] } />
         <Route path="/placeOrder" element={[<Header />,<PlaceOrder/>] } />
          <Route path="/Login" element={[<Header />,<Login/>] } />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
