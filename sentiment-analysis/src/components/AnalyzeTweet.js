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
        return (
            <Container>
                <Row>
                    <Col>
                        <Container id="resultsContainer" fluid>
                            {this.state.sentiment}
                        </Container>
                    </Col>
                    <Col>
                        <Container id="scoreContainer" fluid>
                            {this.state.score}
                        </Container>
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default AnalyzeTweet;