import { createGlobalStyle } from 'styled-components';

export const GlobalStyles = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
    background-color: #FFFFFF;
    color: #333333;
  }
  a {
    color: #333333;
    text-decoration: none;

    &:hover {
      color: #555555;
    }
  }
`;
