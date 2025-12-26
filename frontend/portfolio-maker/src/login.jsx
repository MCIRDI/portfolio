import { useState } from "react";
import "./login.css";
import { Link } from "react-router-dom";
import { login } from "./services/authentication";

function Login() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    login(formData);
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <>
      <main>
        <div className="left-block"></div>
        <div className="right-block">
          <div className="right-block-content">
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <h1>Log in</h1>

                <div className="form-group">
                  <label htmlFor="email">Email</label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="password">Password</label>
                  <input
                    type="password"
                    id="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                  />
                </div>
              </div>

              <button type="submit">Register</button>
            </form>

            <div className="right-block-content-sign">
              <p>Do not have account?</p>
              <Link to="/register">
                <p>Create account!</p>
              </Link>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

export default Login;
