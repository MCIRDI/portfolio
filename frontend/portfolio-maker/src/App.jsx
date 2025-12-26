import "./App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from "./landing.jsx";
import Register from "./register.jsx";
import Login from "./login.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
