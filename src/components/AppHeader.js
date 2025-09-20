import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const Header = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 40px;
  background-color: rgba(255, 255, 255, 0.95); // Nearly opaque white with a hint of transparency
  backdrop-filter: blur(8px); // More pronounced blur effect
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
`;

const Logo = styled.h1`
  font-size: 28px; // Slightly larger for better visibility
  color:rgb(0, 0, 0); // Subtle blue for a modern touch
  font-family: 'Arial', sans-serif; // Clean and professional font choice
  font-weight: bold;
`;

const Nav = styled.nav`
  display: flex;
  align-items: center;
`;

const StyledLink = styled(Link)`
  margin-right: 25px; // More spacing between links
  font-size: 16px;
  color: #666; // Softened the gray for a less harsh look
  text-decoration: none;
  transition: color 0.3s;

  &:hover {
    color:rgb(140, 140, 140); // Blue to match the logo on hover for consistency
  }
`;

const Button = styled(Link)`
  padding: 10px 20px; // Increased padding for a better touch target
  border: 2px solid transparent; // Removing border visibility until hover
  border-radius: 5px; // Slightly rounded for a softer look
  color:rgb(144, 144, 144); // Consistent with logo color
  background-color: transparent; // Clear background to reduce visual clutter
  text-decoration: none;
  transition: all 0.3s ease-in-out;

  &:hover {
    background-color:rgb(140, 140, 140); // Blue background on hover
    color: #fff; // White text on hover
    border-color:rgb(211, 211, 211); // Blue border to match
  }
`;

const AppHeader = () => (
  <Header>
    <Logo>CineCopilot</Logo>
    <Nav>
      <StyledLink to="/">Home</StyledLink>
      <StyledLink to="/features">Features</StyledLink>
      <StyledLink to="/about">About</StyledLink>
      <Button to="/login">Log in</Button>
      <Button to="/signup">Sign up</Button>
    </Nav>
  </Header>
);

export default AppHeader;





