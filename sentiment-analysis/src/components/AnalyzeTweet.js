import React from "react";
import { Col, Row } from "react-bootstrap";
import Container from "react-bootstrap/esm/Container";
import Table from "react-bootstrap/Table"
import { Badge } from "react-bootstrap";
import { Image } from "react-bootstrap";
import { Card } from "react-bootstrap";
import CardHeader from "react-bootstrap/esm/CardHeader";

class AnalyzeTweet extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            result: ""
        }
    }

    reset() {
        this.setState({
            sentiment: "",
            score: ""
        })
    }

    analyzeTweet(msg) {
        console.log(msg)

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ inputTweet: msg })
        };

        fetch("http://127.0.0.1:5000/sentiment", requestOptions).then(res => res.json()).then(res => {
            console.log(res)
            this.setState({ sentiment: res.sentiment, score: res.score })
        }, (error) => { alert(" error while fetching..") })
    }


    render() {
        if(this.state.sentiment) {
            return (
            <Container id="resultsContainer" fluid>
                <Row className="justify-content-md-center" ><Col xs lg="2"><b>Sentiment</b></Col><Col xs lg="2"><b>Score</b></Col></Row>
                <Row className="justify-content-md-center">
                    <Col xs lg="2">
                        <Container>
                            {this.state.sentiment}
                        </Container>
                    </Col>
                    <Col xs lg="2">
                        <Container>
                            {this.state.score}
                        </Container>
                    </Col>
                </Row>
            </Container>
        );
        } else {
            return (
                <Container>
                </Container>
            );
        }
        
    }
}

export default AnalyzeTweet;