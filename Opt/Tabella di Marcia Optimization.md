- ## ==24-25 September==

	~~**Lecture 01 (2hrs):**~~
    
    Introduction to the course, bureaucracy. Definition of a mathematical optimization problem: objective function, decision variables, feasibile set; Example: optimal portfolio selection problem; Classification of optimization problems [GS 1.1]. Optimation problem example: mathematical models estimation; the case of supervised learning - empirical risk minimization problem [GS 1.5, LN 6.1].
    
    ~~**Lecture 02 (2hrs):**~~
    
    Fundamental concepts: global optimizer; Existence of an optimal solution: definition and conditions; Weierstrass Theorem (w/ prf.); Definition of compact sets and the case of the Euclidean space [GS A.3]; Compact level sets, sufficient conditions of existence of a solution (w/ prf.) [GS 1.4].
    
- ## ==1-2 October==
    
    ~~**Lecture 03 (2hrs):**~~
    
    Coercivity, examples of coercive functions: norms, quadratic forms (w/ prf.) [GS 1.4]; Local minimizers; convexity [GS C.1,C.2,C.3].
    
    ~~**Lecture 04 (2hrs):**~~
    
    Optimal solutions in the convex case (w/ prf.), strict convexity, uniqueness of solution in strictly convex case [GS 1.2]. Strong convexity [LN X.XX].  Optimality conditions: overview [GS 2.1]; Preliminaries: differentiable functions [GS Appendix B].
    
- ## ==8-9 October==
    
    ~~**Lecture 05 (2hrs):**~~
    
    Convex differentiable functions [GS Appendix C.5]. Descent directions; first order descent condition, necessary condition of local optimality; first order  necessary condition of optimality (w/ prf.).
    
    ~~**Lecture 06 (2hrs):**~~ 
    
    Descent condition for convex functions (w/ prf.); necessary and sufficient condition of optimality in the convex case (w/ prf.) [GS 2.3]. Negative curvature directions, second order descent condition (w/ prf.) [GS 2.2]. Second order necessary condition of optimality (w/ prf.); second order sufficient conditions of optimality; the case of quadratic functions (w/ prf.)  [GS 2.3].
    
- ## ==15-16 October==
    
    ~~**Lecture 07 (2hrs):**~~ 
    
    Regularized linear regression problems: existence and uniqueness of the solution [LN 6.2]. Optimization algorithms for unconstrained optimization: general scheme of iterative algorithm; sequences of solutions [GS 3.1, LN 4.1]. Baisc principles of line search,  trust region and direct search methods [LN 4.1].  
    Sufficient condition of existence of accumulation points (w\ prf.) [LN 4.1.1]. Infinite convergence towards stationary points [LN 4.1.2]. 
    
    ~~**Lecture 08 (2hrs):**~~ 
    
    Assumptions for convergence towards stationarity: counterexample [LN 4.1.2]. Convergence speed and complexity bounds [LN 4.1.3]. Global and local convergence properties.
    
    Line-search type methods: general scheme; crucial elements for convergence: choice of the direction and the stepsize; counterexample [LN 4.2]. 
    
- ## ==22-23 October==
    
    ~~**Lecture 09 (2hrs):**~~ 
    
    Line searches: general concepts; exact line searches, the quadratic case; inexact line searches, sufficient decrease, Armijo condition; Armijo line search, finite termination properties (w/ prf.) [LN 4.2.1]. 
    
    ~~**Lecture 10 (2hrs):**~~
    
    Gradient-related directions: definition and interpretation; bounded eigenvalues condition [LN 4.2.2]. Global convergence of line search based methods (w/ prf.) [LN 4.2.3]
    
- ## ==29-30 October==
    
    ~~**Lecture 11 (2hrs):**~~ 
    
    L-smoothness, descent lemma; Armijo line search along gradient related directions: interval of surely acceptable stepsizes (w/ prf.); upper bound on backtracks/lower bound on stepsize (w/o prf.); complexity of the algorithmic framework under L-smoothness assumptions (w/ prf.), optimal complexity of first-order methods (w/o prf.).  [LN 4.2.3]. Gradient descent method: algorithmic scheme, convergence properites [GS 6.1-6.2, LN 4.3].  
      
    
    ~~**Lecture 12 (2hrs):**~~ 
    
    Gradient descent with constant stepsize; complexity under convexity assumptions (w/ prf.); convergence rate in the strongly convex case (w/o prf.) [LN 4.3], impact of l2 regularization in machine learning problems [LN 6.1]. Algorithms with momentum terms [LN 4.4], Heavy-ball method [LN 4.4.1].
    
- ## ==5-6 November==
    
    ~~**Lecture 13 (2hrs):**~~ 
    
    Accelerated gradient method [LN 4.4.2]. Nonlinear conjugate direction methods, restarting strategies, Wolfe line search [LN 4.4.3]. 
    
    ~~**Lecture 14 (2hrs):**~~ 
    
    Conjugate gradient method for quadratic problems, finite termination (w/o prf.) [LN 4.4.3]. 
    
    Second order methods, Netwon method as iterative optimization of second order Taylor approximation;  Newton's method does not have global convergence properties: counterexample; Local convergence properties (w/ prf.) [LN 4.5].
    
- ## ==12-13 November==
    
    ~~**Lecture 15 (2hrs):**~~ 
    
    Local convergence properties of Newton's method (continued) [LN X.XX]. Globalization of Newton's method [LN 4.5]. 
    
    Hessian approximation, Quasi-Newton equation, direct and inverse update rules [LN 4.6].
    
    ~~**Lecture 16 (2hrs):~~  
    
    Rank-1 and rank-2 update rules [LN 4.6]; BFGS method [LN 4.6.1]; large scale problems, L-BFGS algorithm [LN 4.6.2].
    
    Constrained optimization problems: feasible directions, necessary optimality conditions [GS 17.2.1].
    
- ## 19-20 November
    
    **Lecture 17 (2hrs):** 
    
    Problems with convex constraints: feasible directions (w/ prf.), optimality conditions (w/ prf.) [GS 17.2.2]. Problems with linear constraints, feasible directions (w/o prf.), optimality conditions with box constraints (w/ prf.) [GS 17.2.3]. Projection onto a convex set: definition, equivalent characterization (w/o prf.), continuity (w/o prf.), stationarity condition basedon projection (w/ prf.) [GS 17.2.4].
    
    **Lecture 18 (2hrs):** 
    
    Projection onto box constraints and ball constraints [GS 17.2.4]. Constrained Armijo type line-search, convergence properties (w/o prf.) [GS 17.3]. Projected gradient method: algorithmic scheme and convergence properties (w/ prf.) [GS 17.5]. Frank-Wolfe method: algorithmic scheme and convergence properties (w/ prf.) [GS 17.4].
    
- ## 26-27 November
    
    **Lecture 19 (2hrs):** 
    
    Optimization problems with analytical constraints [GS D]; Fritz-John conditions [GS D.1]; constraints qualifications, KKT conditions [GS D.2]; LCQ, LICQ (w/ prf.), SCQ; particular case of convex problems with linear constraints [GS D.5].
    
    **Lecture 20 (2hrs):** 
    
    Simplex constraints, optimality condition (w/ prf.) [GS D.5]. Binary classification problems; Support Vector Machines as minimizers of L2-regularized hinge loss minimization, geometrical interpretation [LN 7]; properties of Wolfe dual problem (w/ prf.), derivation of SVM dual formulation (w/ prf.) [LN 7.1].
    
- ## 3-4 December
    
    **Lecture 21 (2hrs):  
    **
    
    Derivation of dual problem (continued), geometrical interpretation of the solution [LN 7.1]. Kernel SVM [LN 7.1]. Decomposition Techniques [LN 4.7, GS 16].
    
    **Lecture 22 (2hrs):** 
    
    Solving SVM dual by decomposition [LN 7.2]; Sequential Minimal Optimization: two-variables update, feasible directions, descent directions, SMO algorithmic scheme, gradients update  [LN 7.2.1]. SVM dual: optimality conditions (w/o prf.), Most Violating Pairs, convergence results for SMO algorithm [LN 7.2.2].
    
- ## 10-11 December
    
    **Lecture 23 (2hrs):  
    **
    
    Finite-sum problems, Stochastic Gradient Descent method [LN 4.8]. Convergence of SGD (w/o prf.), complexity results, Minibatch SGD [LN 4.8.1]; Overview on Deep Networks training: problem characteristics and motivations for minibatch SGD [LN 8].
    
    **Lecture 24 (2hrs):** 
    
    SGD in DL scenario: addition of acceleration terms [LN 8.1.1], adaptive learning rate [LN 8.1.2]. Automatic differentiation and backpropagation [LN 8.2].