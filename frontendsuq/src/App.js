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
function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={[<Header />,<Home/>] } />
      <Route path="/shop" element={[<Header />,<Shop/>] } />
      <Route path="/seller" element={[<Header />,<Seller/>] } />
      <Route path="/itempage" element={[<Header />,<ItemPage/>] } />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
