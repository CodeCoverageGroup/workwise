describe('Sign In', () => {
  beforeEach(() => {
    // Visit the sign-in page before each test
    cy.visit('localhost:3000/authentication/sign-in');
  });


  it('should sign in and redirect to the dashboard', () => {
    // Enter email and password
    cy.get('input[type="text"]').type('gunsu');
    cy.get('input[type="password"]').type('asd123');

    // Submit the form
    cy.get('form').submit();

    // Verify that the user is redirected to the dashboard
    cy.url().should('include', 'localhost:3000/dashboard');
  });

  it('should display an error message for invalid credentials', () => {
    // Enter invalid email password
    cy.get('input[type="text"]').type('invalid@example.com');
    cy.get('input[type="password"]').type('wrongpassword');

    // Submit the form
    cy.get('form').submit();

    // Verify that an error message is displayed
    cy.contains('Login failed. Please check your email and password.').should('be.visible');
  }); 
});

describe('Departments Module', () => {
  beforeEach(() => {
    // Visit the sign-in page and log in
    cy.visit('http://localhost:3000/authentication/sign-in');
    cy.get('input[type="text"]').type('your_username');
    cy.get('input[type="password"]').type('your_password');
    cy.get('form').submit();
    cy.wait(1000); // Wait for the dashboard to load
    cy.url().should('include', '/dashboard'); // Assert that login was successful
    cy.visit('http://localhost:3000/departments');
    cy.url().should('include', '/departments'); // Ensure we are on the correct page
  });

  it('should display the departments table', () => {
    // Check if the departments table is displayed
    cy.get('table').should('exist');
  });

  it('should add a new department', () => {
    // Open the add department modal
    cy.contains('Add Department').click();

    // Fill out the form
    cy.get('input[placeholder="Name"]').type('New Department');
    cy.get('input[placeholder="Description"]').type('This is a new department.');

    // Submit the form
    cy.get('button[type="submit"]').contains('Add Department').click();

    // Wait for the new department to appear and verify it
    cy.contains('New Department').should('be.visible');
    cy.get('table tbody tr').last().should('contain', 'New Department'); // Verify it is added to the table
  });

  it('should view and update a department', () => {
    cy.visit('localhost:3000/departments');
    // Click the "View" button for the first department
    cy.get('table').find('button').contains('View').first().click();
    // Verify that the department details modal is displayed
    cy.contains('View / Edit Department').should('be.visible');
    // Update the department name
    cy.get('input[placeholder="Name"]').clear().type('Updated Department');
    // Submit the form
    cy.get('button').contains('Update Department').click();
    // Verify that the department name is updated
    cy.contains('Updated Department').should('be.visible');
  }); 

  it('should delete a department', () => {
    cy.visit('localhost:3000/departments');
    // Click the "View" button for the first department
    cy.get('table').find('button').contains('View').first().click();
    // Verify that the department details modal is displayed
    cy.contains('View / Edit Department').should('be.visible');
    // Click the delete button
    cy.get('button').contains('Delete Department').click();
    // Verify that the department is deleted
    cy.contains('Department deleted successfully!').should('not.exist');
  }); 
});


describe('Machines Management', () => {
  beforeEach(() => {
    // Visit the sign-in page and log in
    cy.visit('localhost:3000/authentication/sign-in');
    cy.get('input[type="text"]').type('gunsu');
    cy.get('input[type="password"]').type('asd123');
    cy.get('form').submit();
    cy.wait(3000); // Wait for the dashboard to load
    // Navigate to the machines page
    cy.visit('localhost:3000/machines');
  });

  it('should display the machines table', () => {
    // Check if the machines table is displayed
    // cy.contains('Total machines').should('be.visible');
    cy.get('table').should('exist');
  });


  it('should add a new machine', () => {
    cy.contains('Add Machine').click();
    cy.get('input[placeholder="Model Number"]').type('12345');
    cy.get('input[placeholder="Location"]').type('Factory 1');
    cy.get('input[placeholder="Name"]').type('Machine A');
    cy.get('input[placeholder="Description"]').type('Description of Machine A');
    cy.get('button[type="submit"]').contains('Add Machine').click();
    cy.contains('Machine added successfully!').should('be.visible');
  });


  it('should update a machine', () => {
    cy.contains('View').first().click();

    cy.get('input[placeholder="Model Number"]').clear().type('54321');

    cy.get('input[placeholder="Location"]').clear().type('Factory 2');

    cy.get('input[placeholder="Name"]').clear().type('Machine B');

    cy.get('button[type="submit"]').contains('Update Machine').click();

    cy.contains('Machine updated successfully!').should('be.visible');

  });

  it('should delete a machine', () => {
    cy.contains('View').first().click();
    cy.get('button').contains('Delete Machine').click();
    cy.contains('Machine deleted successfully!').should('be.visible');
  });
});