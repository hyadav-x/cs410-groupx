import './App.css';
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import { useRef } from 'react';
import { useState } from 'react';
import Navbar from 'react-bootstrap/Navbar'
import homepageImage from './homepage.png'
import AnalyzeTweet from './components/AnalyzeTweet'

function App() {

  const fref = useRef()
  const [msg, setMessage] = useState("");

  const reset = () => {
    setMessage("")
    fref.current.reset();
  }

  const analyzeTweet = () => {
    if (msg.trim().length > 0) {
      fref.current.analyzeTweet(msg)
    }
  }

  return (
    <Container id="parentContainer" fluid>
      <Container id="navContainer" fluid>
        <Navbar expand="lg" className="navbar-custom" sticky="top">
          <Container id="bannerContainer" fluid>
            <Navbar.Brand href="#" id="title"><img
              src={homepageImage}
              width="120"
              height="50"
            /><span id="titleSpan">Twitter Sentiment Analysis</span></Navbar.Brand>
          </Container>
        </Navbar>
      </Container>

      <Container id="contentContainer">
        <Row>
          <Col>
            <Form>
              <Row className="justify-content-md-center">
                <Col sm lg="6">
                  <Form.Label htmlFor="inlineFormInput" visuallyHidden> Tweet </Form.Label>
                  <Form.Control as="textarea" rows={3} className="mb-2" id="inlineFormInput" placeholder="Enter your tweet here..." value={msg} onChange={e => setMessage(e.target.value)} />
                </Col>
                <Col sm="auto">
                  <Row>
                    <Col><Button id="submitBtn" variant="primary" className="mb-2" onClick={analyzeTweet}>Submit</Button></Col>
                  </Row>
                  <Row>
                    <Col><Button variant="warning" onClick={reset}>Reset</Button></Col>
                  </Row>
                </Col>
              </Row>
              <Row>
                &nbsp;
              </Row>
              <Row>
                <hr></hr>
              </Row>
              <Row>
                &nbsp;
              </Row>
            </Form>
          </Col>
        </Row>
        <Row className="justify-content-md-center">
          <AnalyzeTweet ref={fref}></AnalyzeTweet>
        </Row>
      </Container>
    </Container>
  );
}

export default App;
