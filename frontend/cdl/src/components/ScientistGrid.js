import React from 'react';
import ScientistCard from './ScientistCard';
import data from '../assets/scientists.json';
import { Container, Row, Col } from 'react-bootstrap';

function ScientistGrid() {
  return (
    <Container className="mt-4">
      <Row className="justify-content-center">
        {data.map((sci) => (
          <Col key={sci.id} xs={6} sm={4} md={3} lg={2} className="d-flex justify-content-center">
            <ScientistCard
              name={sci.name}
              image={`/images/${sci.image}`} // ✅ Image path correct if images are in /public/images/
            />
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default ScientistGrid;
