import React from "react";
import { Col, Row } from "react-bootstrap";
import Container from "react-bootstrap/esm/Container";
import Table from "react-bootstrap/Table"
import { Badge } from "react-bootstrap";
import { Image } from "react-bootstrap";
import { Card } from "react-bootstrap";
import CardHeader from "react-bootstrap/esm/CardHeader";
import {HandThumbsUpFill} from  'react-bootstrap-icons';
import {HandThumbsDownFill} from  'react-bootstrap-icons';
import positiveImg from './thumbs-up.png';
import negativeImg from './thumbs-down.png';


class AnalyzeTweet extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            sentiment: "",
            score: ""
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
        if (this.state.sentiment == "positive") {
            return (
                <Card style={{ width: '18rem' }}>
                    <Card.Body>
                        <Card.Title>Positive</Card.Title>
                        <Card.Text>
                            This is an example explanation for why the decision was made to be positive.
                            Maybe we could include which words impacted this decsion?
                        </Card.Text>
                        <Card.Img variant="bottom" class="rounded mx-auto d-block" src={positiveImg} />
                    </Card.Body>
                </Card>
            );
        } else if (this.state.sentiment == "negative") {
            return (
                <Card style={{ width: '18rem' }}>
                    <Card.Body>
                        <Card.Title>Negative</Card.Title>
                        <Card.Text>
                            This is an example explanation for why the decision was made to be negative.
                            Maybe we could include which words impacted this decsion?
                        </Card.Text>
                        <Card.Img variant="bottom" class="rounded mx-auto d-block" src={negativeImg} />
                    </Card.Body>
                </Card>
            );
        } else {
            return (
                <Container></Container>
            );
        }

    }
}

export default AnalyzeTweet;